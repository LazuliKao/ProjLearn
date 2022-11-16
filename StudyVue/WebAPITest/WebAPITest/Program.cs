using Microsoft.AspNetCore.Builder;
using Microsoft.Net.Http.Headers;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Reflection;

var builder = WebApplication.CreateBuilder(args);
// Add services to the container.
builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddCors(options =>
{
    options.AddPolicy("CorsPolicy", builder =>
    {
        //builder.SetIsOriginAllowed()
        builder.WithOrigins(new string[]
        {
            "http://localhost:5173"//允许的请求来源
        }).AllowAnyHeader().AllowAnyMethod().AllowCredentials();
    });
});
var app = builder.Build();
// Configure the HTTP request pipeline.
//if (app.Environment.IsDevelopment())
{//API预览页码
    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.EnableFilter();
        options.EnableTryItOutByDefault();

        //options.InjectJavascript("{appnamespace}.Content.js.translator.js");
        //options.InjectJavascript("{appnamespace}.Content.js.pt.js");
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "v1");
        options.RoutePrefix = string.Empty;
    });
}
app.UseHttpsRedirection();
InitAllApi();//初始化API
app.UseCors("CorsPolicy");
app.UseAuthorization();
app.MapControllers();
app.Run();
void InitAllApi()
{
    Dictionary<string, LoginInfo> tokenMap = new();
    app.MapPost("/login", (LoginRequest data) =>
    {
        if (true)
        {
            string token = Guid.NewGuid().ToString();
            var info = new LoginInfo(data.user);
            tokenMap.Add(token, info);
            Console.WriteLine("新的会话：" + token);
            return new LoginResponse(true, "登录成功", token);
        }
    });
    app.MapPost("/getallitems", (GetAllItemsRequest data) =>
    {
        if (tokenMap.ContainsKey(data.token))
        {
            string token = Guid.NewGuid().ToString();
            var info = new LoginInfo(data.user);
            tokenMap.Add(token, info);
            Console.WriteLine("新的会话：" + token);
            return new LoginResponse(true, "登录成功", token);
        }
        else
        {
            return new { }
        }
    })
    .WithTags("登录");
}
record LoginInfo(string user);
record LoginRequest(string user, string password, string passwordMd5);
record LoginResponse(bool success, string message, string token);

record BaseResponse<T>(bool success, string msg, T data);

record GetAllItemsRequest(string token);
record GetAllItemsResponse() : BaseResponse<List<GetAllItemsResponseItem>>(bool success, string msg);
record GetAllItemsResponseItem();