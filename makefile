.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Intall
	@npm install
	@hugo mod get -u
	@poetry install --no-root
	@poetry run pre-commit install
	@poetry run pre-commit autoupdate


develop: ## Run the site localy
	@hugo server  --minify --disableFastRender --renderToMemory

developfuture: ## Run the site localy with all the future article
	@hugo server  --minify --disableFastRender --buildFuture --renderToMemory

developall: ## Run the site localy with all the article, future or drafts
	@hugo server  --minify --disableFastRender --buildFuture --buildDrafts --renderToMemory

.PHONY: gomodule
gomodule: ## Update Go Module
	@hugo mod get -u ./...
	@hugo mod tidy
	@hugo mod get -u


cache: ## Clean the cache
	@hugo --gc

clean: cach ## Clean the directory of the project of chache e meta file and other things
	@find . -type d -empty -delete

.PHONY: run
run: clean  ## Build the site cleaning all
	@hugo --minify



.PHONY: build
build: clean ## Build for dev
	@hugo mod get -u
	@hugo


deploy: clean ## Ready to deploy
	@npm update
	@poetry export --without-hashes --format=requirements.txt > requirements.txt
	@hugo mod get -u
	@hugo --minify
	@poetry run pre-commit autoupdate


deploy_prod:  ## Ready to deploy
	@npm update
	@hugo mod get -u
	@hugo --minify


.PHONY: submodule
submodule: ## Get submodule for this repo
	git submodule update --init --recursive


precommit: ## Run pre-commit hooks
	@git add . & poetry run pre-commit run --all-files
