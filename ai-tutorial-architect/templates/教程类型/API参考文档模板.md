# API 参考文档模板

> 适用于编写 API 接口文档、SDK 函数说明、命令行工具文档
> 质量目标：准确、完整、易查、示例丰富
> Agent 配置：Writer（主导）+ Fact-Checker（验证）+ Editor（优化）

---

## 🎭 Agent 协作流程

```
[Chief] 确定 API 文档范围和详细程度
    ↓
[@researcher] 收集官方 API 文档和技术资料
    ↓
[@writer] 编写 API 说明、参数定义、示例代码
    ↓
[@fact-checker] 验证所有 API 信息的准确性
    ↓
[@practitioner] 测试示例代码的可运行性
    ↓
[@editor] 优化格式结构，确保易查性
    ↓
[Chief] 审核并定稿
```

---

## 📋 模板使用指南

### 适用场景
- ✅ RESTful API 接口文档
- ✅ SDK/库函数说明
- ✅ 命令行工具(CLI)文档
- ✅ 配置文件说明
- ✅ GraphQL API 文档

### 不适用场景
- ❌ 概念性/教程类内容
- ❌ 架构设计文档
- ❌ 业务流程说明

### 核心特点
- 📚 **参考性**：便于快速查阅
- 🔍 **可搜索**：清晰的索引和分类
- 💻 **可运行**：所有示例经过验证
- 🎯 **准确性**：与实现严格一致

---

# [API 名称] 参考文档

> [一句话描述 API 用途]
> 
> 📚 版本：[版本号] | 📅 最后更新：YYYY-MM-DD | 🔗 基础 URL：`[base_url]`

---

## 📑 文档导航

### 快速链接

| 分类 | API 数量 | 跳转 |
|------|----------|------|
| 📝 **基础接口** | [数量] | [#基础接口](#一基础接口) |
| 👤 **用户相关** | [数量] | [#用户相关接口](#二用户相关接口) |
| 📊 **数据操作** | [数量] | [#数据操作接口](#三数据操作接口) |
| ⚙️ **系统管理** | [数量] | [#系统管理接口](#四系统管理接口) |

### 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| v1.1.0 | YYYY-MM-DD | 新增 [接口名称] 接口 |
| v1.0.0 | YYYY-MM-DD | 初始版本 |

---

## 通用说明

### 基础信息

| 项目 | 说明 |
|------|------|
| **基础 URL** | `[base_url]` |
| **协议** | HTTPS |
| **数据格式** | JSON |
| **字符编码** | UTF-8 |
| **认证方式** | [Bearer Token / API Key / OAuth 2.0] |

### 请求格式

**HTTP 方法**：
- `GET` - 获取资源
- `POST` - 创建资源
- `PUT` - 完整更新资源
- `PATCH` - 部分更新资源
- `DELETE` - 删除资源

**请求头**：
```http
Content-Type: application/json
Authorization: Bearer [token]
X-API-Version: v1
```

### 响应格式

**成功响应**（HTTP 2xx）：
```json
{
  "code": 200,
  "message": "success",
  "data": { ... }
}
```

**错误响应**（HTTP 4xx/5xx）：
```json
{
  "code": 400,
  "message": "error description",
  "error": {
    "type": "ValidationError",
    "details": [ ... ]
  }
}
```

### 状态码说明

| 状态码 | 含义 | 说明 |
|--------|------|------|
| 200 | OK | 请求成功 |
| 201 | Created | 创建成功 |
| 400 | Bad Request | 请求参数错误 |
| 401 | Unauthorized | 未授权 |
| 403 | Forbidden | 禁止访问 |
| 404 | Not Found | 资源不存在 |
| 429 | Too Many Requests | 请求过于频繁 |
| 500 | Internal Server Error | 服务器内部错误 |

---

## 一、基础接口

### 1.1 获取 API 信息

获取 API 的基本信息和状态。

#### 请求

```http
GET /api/v1/info
```

**请求参数**：无

**请求示例**：
```bash
curl -X GET "[base_url]/api/v1/info" \
  -H "Accept: application/json"
```

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "name": "[API名称]",
    "version": "v1.0.0",
    "status": "operational",
    "documentation": "[文档链接]"
  }
}
```

**响应字段说明**：

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | API 名称 |
| `version` | string | 当前版本 |
| `status` | string | 服务状态 |
| `documentation` | string | 文档链接 |

---

### 1.2 健康检查

检查 API 服务是否正常运行。

#### 请求

```http
GET /api/v1/health
```

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "healthy",
  "data": {
    "status": "up",
    "timestamp": "2026-01-28T10:30:00Z",
    "uptime": "99.99%"
  }
}
```

---

## 二、用户相关接口

### 2.1 用户登录

用户登录并获取访问令牌。

#### 请求

```http
POST /api/v1/auth/login
```

**请求头**：
```http
Content-Type: application/json
```

**请求参数**：

| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| `username` | string | 是 | 用户名 | `"user123"` |
| `password` | string | 是 | 密码 | `"********"` |
| `remember` | boolean | 否 | 记住登录 | `true` |

**请求体示例**：
```json
{
  "username": "user123",
  "password": "your_password",
  "remember": true
}
```

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "login success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2g...",
    "expires_in": 3600,
    "user": {
      "id": "usr_123456",
      "username": "user123",
      "email": "user@example.com"
    }
  }
}
```

**响应字段说明**：

| 字段 | 类型 | 说明 |
|------|------|------|
| `token` | string | 访问令牌 |
| `refresh_token` | string | 刷新令牌 |
| `expires_in` | integer | 过期时间（秒） |
| `user` | object | 用户信息 |

**错误响应**：

| 状态码 | 错误码 | 说明 |
|--------|--------|------|
| 400 | `INVALID_PARAMS` | 参数错误 |
| 401 | `INVALID_CREDENTIALS` | 用户名或密码错误 |
| 429 | `TOO_MANY_ATTEMPTS` | 登录尝试次数过多 |

**错误示例**（401 Unauthorized）：
```json
{
  "code": 401,
  "message": "invalid username or password",
  "error": {
    "type": "AuthenticationError",
    "code": "INVALID_CREDENTIALS"
  }
}
```

#### 代码示例

**cURL**：
```bash
curl -X POST "[base_url]/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "user123",
    "password": "your_password"
  }'
```

**JavaScript (Fetch)**：
```javascript
const response = await fetch('[base_url]/api/v1/auth/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    username: 'user123',
    password: 'your_password'
  })
});

const data = await response.json();
console.log(data.data.token);
```

**Python (Requests)**：
```python
import requests

response = requests.post(
    '[base_url]/api/v1/auth/login',
    json={
        'username': 'user123',
        'password': 'your_password'
    }
)

data = response.json()
token = data['data']['token']
```

> **[@practitioner] 验证**：✅ 以上代码已测试通过

---

### 2.2 获取用户信息

获取当前登录用户的详细信息。

#### 请求

```http
GET /api/v1/user/profile
```

**请求头**：
```http
Authorization: Bearer [token]
```

**请求参数**：无

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": "usr_123456",
    "username": "user123",
    "email": "user@example.com",
    "avatar": "https://...",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-28T10:30:00Z"
  }
}
```

---

## 三、数据操作接口

### 3.1 获取资源列表

获取资源的列表，支持分页、排序和筛选。

#### 请求

```http
GET /api/v1/resources
```

**查询参数**：

| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| `page` | integer | 否 | 页码（默认 1） | `1` |
| `limit` | integer | 否 | 每页数量（默认 20） | `20` |
| `sort` | string | 否 | 排序字段 | `-created_at` |
| `filter` | string | 否 | 筛选条件 | `status:active` |
| `search` | string | 否 | 搜索关键词 | `keyword` |

**参数说明**：
- `sort`：字段名前加 `-` 表示降序，如 `-created_at`
- `filter`：格式为 `field:value`，支持多个条件

**请求示例**：
```bash
curl -X GET "[base_url]/api/v1/resources?page=1&limit=20&sort=-created_at" \
  -H "Authorization: Bearer [token]"
```

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [
      {
        "id": "res_001",
        "name": "Resource 1",
        "status": "active",
        "created_at": "2026-01-28T10:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 100,
      "total_pages": 5,
      "has_next": true,
      "has_prev": false
    }
  }
}
```

**响应字段说明**：

| 字段 | 类型 | 说明 |
|------|------|------|
| `items` | array | 资源列表 |
| `pagination.page` | integer | 当前页码 |
| `pagination.limit` | integer | 每页数量 |
| `pagination.total` | integer | 总记录数 |
| `pagination.total_pages` | integer | 总页数 |
| `pagination.has_next` | boolean | 是否有下一页 |
| `pagination.has_prev` | boolean | 是否有上一页 |

---

### 3.2 创建资源

创建新资源。

#### 请求

```http
POST /api/v1/resources
```

**请求头**：
```http
Content-Type: application/json
Authorization: Bearer [token]
```

**请求体参数**：

| 参数 | 类型 | 必填 | 说明 | 验证规则 |
|------|------|------|------|----------|
| `name` | string | 是 | 资源名称 | 长度 1-100 |
| `description` | string | 否 | 资源描述 | 长度 0-500 |
| `status` | string | 否 | 资源状态 | 枚举: active, inactive |
| `tags` | array | 否 | 标签列表 | 最多 10 个 |

**请求示例**：
```json
{
  "name": "My Resource",
  "description": "This is a sample resource",
  "status": "active",
  "tags": ["tag1", "tag2"]
}
```

#### 响应

**成功响应**（201 Created）：
```json
{
  "code": 201,
  "message": "resource created",
  "data": {
    "id": "res_new123",
    "name": "My Resource",
    "description": "This is a sample resource",
    "status": "active",
    "tags": ["tag1", "tag2"],
    "created_at": "2026-01-28T10:30:00Z",
    "updated_at": "2026-01-28T10:30:00Z"
  }
}
```

**错误响应**（400 Bad Request）：
```json
{
  "code": 400,
  "message": "validation failed",
  "error": {
    "type": "ValidationError",
    "details": [
      {
        "field": "name",
        "message": "name is required"
      }
    ]
  }
}
```

---

### 3.3 更新资源

更新指定资源的信息。

#### 请求

```http
PUT /api/v1/resources/{id}
PATCH /api/v1/resources/{id}
```

**路径参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `id` | string | 资源 ID |

**请求体参数**：

与创建资源相同，但所有字段可选。

- `PUT`：完整更新，未提供的字段会被清空或设为默认值
- `PATCH`：部分更新，只更新提供的字段

---

### 3.4 删除资源

删除指定资源。

#### 请求

```http
DELETE /api/v1/resources/{id}
```

**路径参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `id` | string | 资源 ID |

**查询参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `force` | boolean | 否 | 是否强制删除（默认 false） |

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "resource deleted",
  "data": {
    "id": "res_001",
    "deleted_at": "2026-01-28T10:30:00Z"
  }
}
```

---

## 四、系统管理接口

### 4.1 获取系统状态

获取系统运行状态和统计信息。

#### 请求

```http
GET /api/v1/admin/status
```

**权限要求**：管理员

#### 响应

**成功响应**（200 OK）：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "server": {
      "uptime": "30d 12h 34m",
      "load": [0.5, 0.6, 0.7],
      "memory": {
        "total": "16GB",
        "used": "8GB",
        "free": "8GB"
      }
    },
    "database": {
      "connections": 50,
      "queries_per_second": 120
    },
    "cache": {
      "hit_rate": 95.5,
      "size": "2GB"
    }
  }
}
```

---

## 五、数据类型定义

### 通用数据类型

#### User 对象

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 用户唯一标识 |
| `username` | string | 用户名 |
| `email` | string | 邮箱地址 |
| `avatar` | string | 头像 URL |
| `role` | string | 用户角色 |
| `status` | string | 账户状态 |
| `created_at` | string | 创建时间（ISO 8601） |
| `updated_at` | string | 更新时间（ISO 8601） |

#### Resource 对象

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 资源唯一标识 |
| `name` | string | 资源名称 |
| `description` | string | 资源描述 |
| `status` | string | 资源状态 |
| `tags` | array | 标签列表 |
| `created_at` | string | 创建时间 |
| `updated_at` | string | 更新时间 |

### 枚举类型

#### 用户角色 (UserRole)

| 值 | 说明 |
|------|------|
| `admin` | 管理员 |
| `user` | 普通用户 |
| `guest` | 访客 |

#### 资源状态 (ResourceStatus)

| 值 | 说明 |
|------|------|
| `active` | 激活 |
| `inactive` | 未激活 |
| `deleted` | 已删除 |

---

## 六、错误代码参考

### 错误代码列表

| 错误代码 | HTTP 状态码 | 说明 | 解决方案 |
|----------|-------------|------|----------|
| `INVALID_PARAMS` | 400 | 请求参数错误 | 检查参数格式和必填项 |
| `INVALID_CREDENTIALS` | 401 | 认证信息错误 | 检查用户名密码或 Token |
| `TOKEN_EXPIRED` | 401 | Token 已过期 | 使用 refresh_token 刷新 |
| `INSUFFICIENT_PERMISSIONS` | 403 | 权限不足 | 检查用户角色和权限 |
| `RESOURCE_NOT_FOUND` | 404 | 资源不存在 | 检查资源 ID 是否正确 |
| `RATE_LIMIT_EXCEEDED` | 429 | 请求过于频繁 | 降低请求频率 |
| `INTERNAL_ERROR` | 500 | 服务器内部错误 | 稍后重试或联系支持 |

---

## 七、SDK 使用指南

### 官方 SDK

| 语言 | 包名 | 安装命令 | 文档 |
|------|------|----------|------|
| JavaScript | `@example/api-sdk` | `npm install @example/api-sdk` | [链接] |
| Python | `example-api-sdk` | `pip install example-api-sdk` | [链接] |
| Go | `github.com/example/api-sdk` | `go get github.com/example/api-sdk` | [链接] |

### JavaScript SDK 示例

```javascript
import { Client } from '@example/api-sdk';

const client = new Client({
  baseURL: '[base_url]',
  token: 'your_token'
});

// 获取资源列表
const resources = await client.resources.list({
  page: 1,
  limit: 20
});

// 创建资源
const newResource = await client.resources.create({
  name: 'New Resource',
  status: 'active'
});
```

---

## ✅ API 文档检查清单

> **[@fact-checker] 验证项**：

- [ ] 所有 API 端点 URL 正确
- [ ] 所有 HTTP 方法正确
- [ ] 所有参数说明完整
- [ ] 所有响应字段说明完整
- [ ] 所有示例代码可运行
- [ ] 错误代码列表完整
- [ ] 数据类型定义准确

> **[@editor] 审核项**：

- [ ] 结构清晰，便于查阅
- [ ] 示例丰富，覆盖常见场景
- [ ] 参数表格格式统一
- [ ] 代码高亮正确

---

*基于 AI Tutorial Architect API 参考文档模板 v1.0.0*
*最后更新：2026-01-28*
