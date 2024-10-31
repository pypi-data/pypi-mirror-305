#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-2.0-only
import signal
import time
import os
import errno
import subprocess

from funnylog2 import logger
from os.path import abspath
from os.path import dirname
from contextlib import contextmanager
from Xlib.display import Display


def recording_screen(name, job_dir=None):
    """
     录制视频
    :param name: 视频名称
    :return:
    """
    logger.info("开始录屏")
    if job_dir is None:
        job_dir = dirname(dirname(abspath(__file__)))
    record_path = (
        f'{job_dir}/report/record/{time.strftime("%Y-%m-%d", time.localtime())}/'
    )
    if not os.path.exists(record_path):
        os.makedirs(record_path)

    _display = Display(os.environ['DISPLAY'])
    width = _display.screen().width_in_pixels
    height = _display.screen().height_in_pixels
    cmd, paths = _create_ffmpeg_cmd(
        width,
        height,
        record_path,
        f"{name.encode('utf-8').decode('unicode-escape')[:40].replace('/', '_')}_autotest",
    )

    for path in paths:
        with suppress(OSError, errnos=(errno.ENOENT, errno.ENAMETOOLONG)):
            os.remove(path)
        logger.info(f"录屏路径存放  {path}")

    with open(os.devnull, "w", encoding="utf-8") as dev_null:
        with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=dev_null, stderr=dev_null, close_fds=True) as proc:
            time.sleep(0.5)
            if proc.poll() is not None:
                raise RuntimeError("ffmpeg did not start")

            try:
                yield paths[0]
            finally:
                logger.info("停止录屏")
                try:
                    os.kill(proc.pid, signal.SIGINT)
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    logger.warning("ffmpeg did not stop gracefully, sending SIGKILL")
                    os.kill(proc.pid, signal.SIGKILL)
                    proc.wait()
                finally:
                    if not proc.stdin.closed:
                        proc.stdin.close()
                    logger.info(f"停止录屏 finish {proc.stdin.closed}")


def _create_ffmpeg_cmd(width, height, dir_path, file_name, qp=1):
    """
     组装ffmpeg命令行参数
    :param width: 宽
    :param height: 高
    :param dir_path: 视频路径
    :param file_name: 视频名称
    :param qp:
    :return:
    """
    cmd = ["ffmpeg"]

    wh = f"{width}x{height}"
    cmd.extend(
        [
            "-framerate",
            "25",
            "-video_size",
            wh,
            "-f",
            "x11grab",
            "-i",
            f"{os.environ.get('DISPLAY', None)}",
        ]
    )

    paths = []
    file_path = os.path.join(dir_path, file_name + "{}.mp4")
    output_fmt = ["-c:v", "libx264", "-qp", str(qp), "-preset", "ultrafast"]
    path = file_path.format("")
    cmd.extend(output_fmt + [path])
    paths.append(path)
    logger.debug(" ".join(cmd))
    return cmd, paths


@contextmanager
def suppress(exception, errnos):
    """
     抛异常
    :param exception:
    :param errnos:
    :return:
    """
    try:
        yield
    except exception as e:
        # logger.error(f"异常 {e}")
        if errno and e.errno not in errnos:
            logger.debug("step 2")
            raise
