define({ "api": [
  {
    "type": "post",
    "url": "//api_0_8/register",
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
          "content": "{ id: 2016212039,\n  password: 123456}",
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
          "content": "{ name: XXX,\n  id: 2016212039}",
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
        "url": "http://www.example.com//api_0_8/register"
      }
    ]
  }
] });
