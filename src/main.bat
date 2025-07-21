@echo off
title fastAPI application with sentry.io integration

COLOR E

pushd ..

set /p environment_name=<_conda_env_name.ini
echo Setting up environment: %environment_name%

call activate %environment_name%

if %errorlevel% neq 0 (
    echo.
    echo Error: Unable to run conda environment: %environment_name%.
    echo.
    pause
    goto end
)

echo Running Python script: src/main.py
uvicorn src.main:app --reload



if %errorlevel% neq 0 (
    echo.
    echo Error: Python script ends with an error.
    echo.
    pause
    goto end
)

echo Skript successfully done.
pause

:end
