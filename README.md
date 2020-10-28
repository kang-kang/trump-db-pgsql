- 此版本不支持数据库主从功能
# trump + postgresql
    此分支支持pgsql数据库，实际使用过程遇到问题请及时联系开发者
### 新增功能： 访问控制列表从数据库读取
- acl_white 当程序中acl为空，黑白名单从数据库读取，结构如下：

| 字段 | ID   |  NAME  | METHOD | ROLENAME  |
| --------   | :-----  | :----:  |  :----   | :----   |
| 类型 | serial | text | text | text[]  |
| 数据 |1 | tests | LS | ["USER","ANONYMOUS"]|
| 数据 |2 | users |GET |	["USER","ANONYMOUS"] |

- 创建语句：

```
CREATE TABLE public.acl_white (
	id serial NOT NULL,
	"name" text NULL,
	"method" text NULL,
	rolename text[] NULL,
	CONSTRAINT acl_white_pkey PRIMARY KEY (id)
)
WITH (
	OIDS=FALSE
) ;
```
------
- 插入语句

```
INSERT INTO public.acl_white("name", "method", rolename) VALUES('users', 'LS', '{user,ANONYMOUS}');
```
