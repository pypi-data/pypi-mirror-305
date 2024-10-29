# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

from dyff.schema.platform import MethodBase, MethodImplementationKind, Report

from .._internal import fqn
from . import context, jupyter, legacy, python


# https://stackoverflow.com/a/38662876/3709935
def _remove_ansi_escape_sequences(line):
    # ansi_escape = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", line)


def run_analysis(method: MethodBase, *, storage_root: Path, config_file: Path):
    # Need this to get the ID assigned to the analysis
    analysis_id = context.id_from_config_file(config_file)

    pythonpath = os.pathsep.join(
        str(storage_root / module) for module in method.modules
    )
    env = os.environ.copy()
    env.update(
        {
            "DYFF_AUDIT_LOCAL_STORAGE_ROOT": str(storage_root),
            "DYFF_AUDIT_ANALYSIS_CONFIG_FILE": str(config_file),
            "PYTHONPATH": pythonpath,
        }
    )

    if method.implementation.kind == MethodImplementationKind.JupyterNotebook:
        impl_module, impl_name = fqn(jupyter.run_jupyter_notebook)
    elif method.implementation.kind == MethodImplementationKind.PythonFunction:
        impl_module, impl_name = fqn(python.run_python_function)
    elif method.implementation.kind == MethodImplementationKind.PythonRubric:
        impl_module, impl_name = fqn(python.run_python_rubric)
    else:
        raise NotImplementedError(
            f"method.implementation.kind = {method.implementation.kind}"
        )

    log_file = storage_root / analysis_id / ".dyff" / "logs.txt"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(log_file, "wb", buffering=0) as fout:
            cmd = f"from {impl_module} import {impl_name}; {impl_name}()"
            subprocess.run(
                ["python3", "-u", "-X", "faulthandler", "-c", cmd],
                env=env,
                check=True,
                # Redirect both streams to log file
                stdout=fout,
                stderr=subprocess.STDOUT,
            )
    finally:
        # Output from Jupyter notebooks often has ANSI escape sequences in it.
        # We want to remove these sequences, but without shadowing the original
        # exception (if any) and without leaving a moment where the logs.txt
        # file could be lost if there's another error.
        current_exception = sys.exc_info()[1]
        try:
            scratch_file = Path(str(log_file) + ".tmp")
            with open(log_file, "r") as fin:
                with open(scratch_file, "w") as fout:
                    fout.writelines(_remove_ansi_escape_sequences(line) for line in fin)
            scratch_file.rename(log_file)
        except Exception as ex:
            if not current_exception:
                raise ex


def run_report(report: Report, *, storage_root: Path):
    return legacy_run_report(
        rubric=report.rubric,
        dataset_path=str(storage_root / report.dataset),
        evaluation_path=str(storage_root / report.evaluation),
        output_path=str(storage_root / report.id),
        modules=[str(storage_root / module) for module in report.modules],
    )


def legacy_run_report(
    *,
    rubric: str,
    dataset_path: str,
    evaluation_path: str,
    output_path: str,
    modules: Optional[list[str]] = None,
):
    if modules is None:
        modules = []

    def quote(s) -> str:
        return f'"{s}"'

    args = [
        quote(rubric),
        quote(dataset_path),
        quote(evaluation_path),
        quote(output_path),
        ", ".join(quote(module) for module in modules),
    ]

    impl_module, impl_name = fqn(legacy.run_python_rubric)
    cmd = (
        f"from {impl_module} import {impl_name}; {impl_name}"
        "(rubric={}, dataset_path={}, evaluation_path={}, output_path={}, modules=[{}])".format(
            *args
        )
    )

    pythonpath = os.pathsep.join(str(module) for module in modules)
    env = os.environ.copy()
    env.update({"PYTHONPATH": pythonpath})

    log_file = Path(output_path) / ".dyff" / "logs.txt"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with open(log_file, "wb", buffering=0) as fout:
        subprocess.run(
            ["python3", "-u", "-X", "faulthandler", "-c", cmd],
            env=env,
            check=True,
            # Redirect both streams to log file
            stdout=fout,
            stderr=subprocess.STDOUT,
        )


__all__ = [
    "legacy_run_report",
    "run_analysis",
    "run_report",
]
