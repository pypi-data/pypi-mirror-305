import asyncio
import pathlib
import shutil


async def copy_file(input_path: pathlib.Path, output_path: pathlib.Path, force: bool = False) -> pathlib.Path | None:
    if input_path.exists():
        if not force:
            return output_path
    try:
        shutil.copy2(input_path, output_path)
    except Exception as e:
        return None

    return output_path


async def run_command(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    return stdout.decode(), stderr.decode(), process.returncode


async def run_cmds(cmds_list):
    tasks = [run_command(cmd) for cmd in cmds_list]
    results = await asyncio.gather(*tasks)
    all_success = all(returncode == 0 for _, _, returncode in results)

    return results, all_success
