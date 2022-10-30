all:
gh-build: install-theme build
install-theme:
	mkdir -p themes/hugo-geekdoc
	curl -L https://github.com/thegeeklab/hugo-geekdoc/releases/latest/download/hugo-geekdoc.tar.gz | tar -xz -C themes/hugo-geekdoc/ --strip-components=1
build:
	hugo
clean:
	rm -r public/
