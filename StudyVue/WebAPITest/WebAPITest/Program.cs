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
    //
}
app.UseHttpsRedirection();
InitAllApi();//��ʼ��API
app.UseCors("CorsPolicy");
app.UseAuthorization();
app.MapControllers();
app.Run();
void InitAllApi()
{
    app.MapGet("/add", () =>
    {
        return new
        {
            a = "233"
        };
    })
    .WithTags("����");
    app.MapGet("/remove", () =>
    {
        return new
        {
            b = "233"
        };
    })
    .WithTags("����2");
}
//record AddResult(string? a  );