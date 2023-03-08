pull:
	git pull --recurse-submodules

push:
	git pull
	cd src/plugins/nonebot_plugin_setu_collection && \
	git push origin HEAD:master