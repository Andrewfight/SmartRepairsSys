define({ "api": [
  {
    "type": "get",
    "url": "/api_0_8/token",
    "title": "用户token",
    "group": "User",
    "description": "<p>请求该接口获取用户token,token生存期为两天。<br></br> <strong>注意：该接口使用http Basic认证，需要在客户端将用户id和密码进行base64编码并添加当请求头Authorization中</strong></p>",
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "int",
            "optional": false,
            "field": "expiration",
            "description": "<p>token生存期</p>"
          },
          {
            "group": "200",
            "type": "timeStamp",
            "optional": false,
            "field": "timeStamp",
            "description": "<p>token生成的时间戳</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "测试样例：",
          "content": "{\n \"expiration\": 172800,\n \"timeStamp\": 1502810538.668,\n \"token\": \"eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMjk4MzMzOCwiaWF0IjoxNTAyODEwNTM4fQ.eyJpZCI6MjAxNjIxMjAzOX0.XbzmXyaZyasmvQVHCvr1i3b3otQ7CuC_X7i6t1kWRBY\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "UserNotFound",
            "description": "<p>用户id或密码错误</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "返回样例：",
          "content": "{ error: unauthorized,\n  message: unauthorized access}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/auth/api_0_8/authentic.py",
    "groupTitle": "User",
    "name": "GetApi_0_8Token",
    "sampleRequest": [
      {
        "url": "http://www.example.com/api_0_8/token"
      }
    ]
  },
  {
    "type": "post",
    "url": "/api_0_8/register",
    "title": "注册用户",
    "group": "User",
    "description": "<p>请求该接口注册新用户</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "id",
            "description": "<p>学号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "测试样例：",
          "content": "{\n  id: 2016212039,\n  password: 123456\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>用户姓名</p>"
          },
          {
            "group": "200",
            "type": "string",
            "optional": false,
            "field": "id",
            "description": "<p>用户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "测试样例：",
          "content": "{\n  name: XXX,\n  id: 2016212039\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "UserNotFound",
            "description": "<p>用户<code>id</code>或密码错误</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "返回样例：",
          "content": "{ error: not found,\n  message: id or password is wrong}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/auth/api_0_8/authentic.py",
    "groupTitle": "User",
    "name": "PostApi_0_8Register",
    "sampleRequest": [
      {
        "url": "http://www.example.com/api_0_8/register"
      }
    ]
  }
] });
