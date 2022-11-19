help:
	@echo "-- Usage --"
	@echo "gh-build"
	@echo "install-theme"
	@echo "build"
	@echo "serve"
	@echo "clean"
gh-build: install-theme build
install-theme:
	mkdir -p themes/hugo-geekdoc
	curl -L https://github.com/thegeeklab/hugo-geekdoc/releases/latest/download/hugo-geekdoc.tar.gz | tar -xz -C themes/hugo-geekdoc/ --strip-components=1
build:
	hugo
serve:
	hugo -D serve
clean:
	rm -r public/
