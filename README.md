# vscode-remote-glibc-patch

Patch glibc on legacy Linux systems to enable compatibility with the latest VSCode Remote.

## Why

Since VSCode 1.99, the Remote-SSH extension pack requires glibc 2.28 or later. This is a problem for many legacy Linux systems that are stuck on older versions of glibc/kernel.

A workaround was provided by [official docs](https://code.visualstudio.com/docs/remote/faq#_can-i-run-vs-code-server-on-older-linux-distributions), which, while helpful, takes a lot of time to compile and configure. This project hence pre-compiles the artifacts and provides a simple script to patch glibc on legacy systems.

## How to use

### Download the appropriate tarball

Find your Linux kernel version via `uname -r`. For example, on CentOS-7 it might be

```
$ uname -r
3.10.0-1160.118.1.el7.x86_64
```

Go to the [Release Page](https://github.com/hsfzxjy/vscode-remote-glibc-patch/releases/tag/BUILD) and download the tarball with kernel version **less than or equal** to the one you found via `uname -r`. For the example above, you should download `x86_64-kernel-3.4.113-gcc-8.5.0-glibc-2.28.tgz`.

### Extract the tarball

Extract the tarball such that it forms such a directory structure:

```
your/custom/path/
├── init.sh
├── patchelf
├── ...
```

where `your/custom/path` could be chosen arbitrarily.

### Modify your shell profiles

Add the following lines to your shell profile:

```bash
eval "$(your/custom/path/init.sh)"
```

Depending on your use case, you may want to modify `~/.bashrc`/`~/.bash_profile` (for yourself only) or `/etc/bashrc`/`/etc/profile` (for all users).

## Contributing

If the provided artifacts won't meet your OS/kernel/arch combination, feel free to create an issue and I will add them!
