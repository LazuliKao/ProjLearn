using Microsoft.AspNetCore.Builder;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Reflection;

var builder = WebApplication.CreateBuilder(args);
// Add services to the container.
builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
var app = builder.Build();
// Configure the HTTP request pipeline.
//if (app.Environment.IsDevelopment())
{//APIÔ¤ÀÀÒ³Âë
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
InitAllApi();//³õÊ¼»¯API
app.UseAuthorization();
app.MapControllers();
app.Run();
void InitAllApi()
{
    app.MapGet("/add", () =>
    {
        return new
        {
            a="a"
        };
    })
    .WithName("add");
}
//record AddResult(string? a  );