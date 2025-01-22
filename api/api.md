
- **统一响应格式**
```typescript
export interface ApiResponse<T> {
    code: number        // 状态码
    message: string     // 响应消息
    data: T            // 响应数据
    timestamp: number  // 响应时间戳
}
```

- **分页查询**
对于查询接口，添加分页参数：
```typescript
export interface PageRequest {
    page: number    // 页码，从1开始
    size: number   // 每页大小
    sort?: string    // 排序字段
}

export interface PageResponse<T> {
    totalElements: number      // 总记录数
    totalPages: number      // 总页数
    content: T[]         // 当前页数据
    number: number   // 页码
    size: number  // 每页大小
    first: boolean     // 是否是第一页
    last: boolean      // 是否是最后一页
}
```
例如:
```http request
POST /api/users/page?page=0&size=10&sort=createTime,desc&sort=username,asc
Content-Type: application/json
```
