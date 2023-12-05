# Mkdocs Material Social Testing

This site is for testing the Mkdocs Material Social links.

Here is our website:

[https://dmccreary.github.io/mkdocs-material-social/](https://dmccreary.github.io/mkdocs-material-social/)


```sh
conda deactivate
conda create -n mkdocs python=3
conda activate mkdocs
pip install mkdocs "mkdocs-material[imaging]"
```

## Checking Libraries

```sh
pip freeze
```

```
Babel==2.13.1
cairocffi==1.6.1
CairoSVG==2.7.1
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
cssselect2==0.7.0
defusedxml==0.7.1
ghp-import==2.1.0
idna==3.6
Jinja2==3.1.2
Markdown==3.5.1
MarkupSafe==2.1.3
mergedeep==1.3.4
mkdocs==1.5.3
mkdocs-material==9.4.14
mkdocs-material-extensions==1.3.1
packaging==23.2
paginate==0.5.6
pathspec==0.11.2
Pillow==9.5.0
platformdirs==4.0.0
pycparser==2.21
Pygments==2.17.2
pymdown-extensions==10.5
python-dateutil==2.8.2
PyYAML==6.0.1
pyyaml_env_tag==0.1
regex==2023.10.3
requests==2.31.0
setuptools==68.0.0
six==1.16.0
tinycss2==1.2.1
urllib3==2.1.0
watchdog==3.0.0
webencodings==0.5.1
wheel==0.41.2
```

## Cairo Library Problems on Mac M2

Errors:

OSError: no library called "cairo-2" was found
no library called "cairo" was found
no library called "libcairo-2" was found

https://github.com/squidfunk/mkdocs-material/issues/5121

```sh
brew install cairo freetype libffi libjpeg libpng zlib
```

I had to add the following line to my .zshrc file:

```sh
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

## Other Notes

cp libcairo.2.dylib /usr/local/bin
Password:
(social) 1.18.0/lib $ pwd
/opt/homebrew/Cellar/cairo/1.18.0/lib

$ brew link cairo -v
Linking /opt/homebrew/Cellar/cairo/1.18.0... 
ln -s ../Cellar/cairo/1.18.0/bin/cairo-trace cairo-trace
ln -s ../Cellar/cairo/1.18.0/include/cairo cairo
ln -s ../Cellar/cairo/1.18.0/lib/cairo cairo
ln -s ../Cellar/cairo/1.18.0/lib/libcairo-gobject.2.dylib libcairo-gobject.2.dylib
ln -s ../Cellar/cairo/1.18.0/lib/libcairo-gobject.dylib libcairo-gobject.dylib
ln -s ../Cellar/cairo/1.18.0/lib/libcairo-script-interpreter.2.dylib libcairo-script-interpreter.2.dylib
ln -s ../Cellar/cairo/1.18.0/lib/libcairo-script-interpreter.dylib libcairo-script-interpreter.dylib
ln -s ../Cellar/cairo/1.18.0/lib/libcairo.2.dylib libcairo.2.dylib
ln -s ../Cellar/cairo/1.18.0/lib/libcairo.dylib libcairo.dylib
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-fc.pc cairo-fc.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-ft.pc cairo-ft.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-gobject.pc cairo-gobject.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-pdf.pc cairo-pdf.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-png.pc cairo-png.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-ps.pc cairo-ps.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-quartz-font.pc cairo-quartz-font.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-quartz-image.pc cairo-quartz-image.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-quartz.pc cairo-quartz.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-script-interpreter.pc cairo-script-interpreter.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-script.pc cairo-script.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-svg.pc cairo-svg.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-tee.pc cairo-tee.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-xcb-shm.pc cairo-xcb-shm.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-xcb.pc cairo-xcb.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-xlib-xrender.pc cairo-xlib-xrender.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo-xlib.pc cairo-xlib.pc
ln -s ../../Cellar/cairo/1.18.0/lib/pkgconfig/cairo.pc cairo.pc

https://github.com/dora-metrics/pelorus/issues/1073

## Sample Markup for an Image:

```markdown

```