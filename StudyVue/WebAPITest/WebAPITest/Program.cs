using Microsoft.AspNetCore.Builder;
using Microsoft.Net.Http.Headers;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Reflection;
using System.Xml.Linq;

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
            "http://localhost:5173"//�����������Դ
        }).AllowAnyHeader().AllowAnyMethod().AllowCredentials();
    });
});
var app = builder.Build();
// Configure the HTTP request pipeline.
//if (app.Environment.IsDevelopment())
{//APIԤ��ҳ��
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
InitAllApi();//��ʼ��API
app.UseCors("CorsPolicy");
app.UseAuthorization();
app.MapControllers();
app.Run();

[global::System.Diagnostics.CodeAnalysis.RequiresUnreferencedCodeAttribute("Calls Microsoft.AspNetCore.Builder.EndpointRouteBuilderExtensions.MapPost(String, Delegate)")]
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
            Console.WriteLine("�µĻỰ��" + token);
            return new LoginResponse(true, "��¼�ɹ�", token);
        }
    });
    app.MapPost("/getallitems", (GetAllItemsRequest data) =>
    {
        if (data is not null and { token: not null } && tokenMap.ContainsKey(data.token))
        {
            Console.WriteLine("call getallitems");
            return new GetAllItemsResponse()
            {
                new GetAllItemsResponseItem("001","������Ʒ1",1,"����1"),
                new GetAllItemsResponseItem("002","������Ʒ2",2,"����2"),
                new GetAllItemsResponseItem("003","������Ʒ3",10,"test3"+DateTime.Now.ToString("G"))
            };
        }
        else
        {
            return null;
        }
    })
    .WithTags("");
    app.MapPost("/getcartitems", (GetAllItemsRequest data) =>
    {
        if (data is not null and { token: not null } && tokenMap.ContainsKey(data.token))
        {
            Console.WriteLine("call getcartitems");
            return new GetAllItemsResponse()
            {
                new GetAllItemsResponseItem("002","������Ʒ2",2,"����2"),
            };
        }
        else
        {
            return null;
        }
    })
    .WithTags("");
}
record LoginInfo(string user);
record LoginRequest(string user, string password, string passwordMd5);
record LoginResponse(bool success, string message, string token);

//record BaseResponse<T>(bool success, string msg, T data);

record GetAllItemsRequest(string token);
class GetAllItemsResponse : List<GetAllItemsResponseItem> { };//BaseResponse<List<GetAllItemsResponseItem>>(bool success, string msg);
record GetAllItemsResponseItem(string id, string name,int price, string description, int number = 0);