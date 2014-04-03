favicon-service for SAE
=================

favicon图标获取服务
---------------

 1. 需要SAE支持，移植至其他云端也比较方便，包含了图标抓取和图标缓存功能（默认不进行缓存清理）
 2. 需要memcache与storage支持
 3. 需要在handler中进行简单的配置

局限
--

没有进行HTML解析，只是暴力的去获取域名下的favicon.ico