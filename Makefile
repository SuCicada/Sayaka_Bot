pull:
	git pull --recurse-submodules

push:
	cd src/plugins/nonebot_plugin_setu_collection && \
	git push origin HEAD:master
	git push