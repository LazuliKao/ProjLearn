using SCI_LazuliKao_MAUI.ViewModels;
using System.IO;

namespace SCI_LazuliKao_MAUI;

public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
        try
        {
            var path = Path.Combine(System.Environment.GetFolderPath(System.Environment.SpecialFolder.Personal), "data.json");
            if (File.Exists(path))
            {
                var text = File.ReadAllText(path);
                var data = Newtonsoft.Json.JsonConvert.DeserializeObject<MainPageViewModel>(text);
                foreach (var item in data.Items)
                {
                    item.RemoveThisFunc = x =>
                    {
                        data.Items.Remove(x);
                    };
                }
                this.BindingContext = data;
            }
        }
        catch (Exception)     {  }
    }
}

