## Installation

You can install the Fiscus SDK via `pip`:

```bash
pip install fiscus --pre
```
*Note: The `--pre` flag is necessary because the SDK is currently in alpha.*

## System Requirements

- **Operating Systems:** Windows, macOS, Linux
- **Python Versions:** 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

## Troubleshooting

### Installation Errors

- **Compiler Not Found:** If you encounter errors related to missing compilers, ensure that you are installing a pre-built wheel. If a wheel is not available for your platform and Python version, you may need to install a C compiler.

  - **Windows:** Install Microsoft Visual C++ Build Tools.
  - **macOS:** Xcode Command Line Tools should be installed.
  - **Linux:** Install `build-essential` (Debian/Ubuntu) or `gcc` (CentOS/Fedora).

### Common Issues

- **Permission Errors:** Ensure you have the necessary permissions to install packages. You might need to use `sudo` or install within a virtual environment.
- **Proxy Issues:** If you're behind a proxy, configure `pip` to use your proxy settings.

## License

The Fiscus SDK is a proprietary software product developed by Fiscus Flows, Inc.

By using this SDK, you agree to the terms and conditions outlined in the [LICENSE](LICENSE) file included with the distribution.

For any questions regarding licensing, please contact us at [support@fiscusflows.com](mailto:support@fiscusflows.com).
