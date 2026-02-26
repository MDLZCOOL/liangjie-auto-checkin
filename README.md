# liangjie-auto-checkin

量界智算自动签到领tokens

https://liangjiewis.com/

Fork 下来后，在`Settings`-`Secrets and Variables`-`Actions`中添加Repository secrets，名字是`LIANGJIE_COOKIE`，内容为

```plaintext
session=XXXXXXX
```

这个需要自己去抓Cookie，后面如果过期了，需要重新抓，然后更新`LIANGJIE_COOKIE`。

[MIT License](LICENSE)