using Newtonsoft.Json;
using Prism.Commands;
using Prism.Mvvm;
using System.Collections.ObjectModel;
using System.Windows.Input;

namespace SCI_LazuliKao_MAUI.ViewModels
{
    public class MainPageViewModel : BindableBase
    {
        public MainPageViewModel()
        {
            //base.PropertyChanged += (s, p) =>
            //{
            //    p.PropertyName
            //}
            CurrentItem = new(RemoveItem);
            foreach (var item in Items)
            {
                DisplayItems.Add(item);
            }
            Items.CollectionChanged += (_, _) =>
            {
                InvokeSearch();
            };
            Items.CollectionChanged += (_, _) =>
            {
                //保存
                //try
                //{ 
                var text = JsonConvert.SerializeObject(Items, Newtonsoft.Json.Formatting.Indented);
                File.WriteAllText(FileLocation, text);
                //}
                //catch (Exception) { }
            };
        }
        private void RemoveItem(AutoPartViewModel item)
        {
            Items.Remove(item);
            DisplayItems.Remove(item);
        }
        private AutoPartViewModel currentItem;
        [JsonIgnore]
        public AutoPartViewModel CurrentItem
        {
            get { return currentItem; }
            set { SetProperty(ref currentItem, value); }
        }
        public ObservableCollection<AutoPartViewModel> Items { get; } = new();
        [JsonIgnore]
        public ObservableCollection<AutoPartViewModel> DisplayItems { get; } = new();
        private DelegateCommand _add;
        public DelegateCommand Add =>
            _add ??= new DelegateCommand(() =>
            {
                if (string.IsNullOrWhiteSpace(CurrentItem.Code))
                {
                    Tip = "请填写编号";
                    return;
                }
                if (string.IsNullOrWhiteSpace(CurrentItem.Name))
                {
                    Tip = "请填写名称";
                    return;
                }
                if (string.IsNullOrWhiteSpace(CurrentItem.Type))
                {
                    Tip = "请填写类型";
                    return;
                }
                if (CurrentItem.Count <= 0)
                {
                    Tip = "数量无效";
                    return;
                }
                Items.Add(CurrentItem);
                Tip = $"添加成功 : {CurrentItem.Code} {CurrentItem.Name} {CurrentItem.Type} {CurrentItem.Count}";
                CurrentItem = new AutoPartViewModel(RemoveItem);
            });
        private DelegateCommand _search;
        public DelegateCommand Search =>
            _search ??= new DelegateCommand(() =>
            {
                searchStarted = true;
                InvokeSearch();
            });
        [JsonIgnore] private bool searchByName;
        public bool SearchByName
        {
            get { return searchByName; }
            set
            {
                if (!value && !SearchByCode)
                    SearchByCode = true;
                SetProperty(ref searchByName, value);
            }
        }
        [JsonIgnore] private bool searchByCode = true;
        public bool SearchByCode
        {
            get { return searchByCode; }
            set
            {
                if (!value && !SearchByName)
                    SearchByName = true;
                SetProperty(ref searchByCode, value);
            }
        }
        [JsonIgnore] private string searchText;
        public string SearchText
        {
            get { return searchText; }
            set
            {
                SetProperty(ref searchText, value);
                InvokeSearch();
            }
        }
        [JsonIgnore] private string tip = "点击入库添加";
        public string Tip
        {
            get { return tip; }
            set { SetProperty(ref tip, value); }
        }
        [JsonIgnore] public string FileLocation => Path.Combine(System.Environment.GetFolderPath(System.Environment.SpecialFolder.Personal), "data.json");
        private bool searchStarted = false;
        public void InvokeSearch()
        {
            if (!searchStarted || string.IsNullOrWhiteSpace(SearchText))
            {
                foreach (var item in Items.Except(DisplayItems).ToArray())
                {
                    DisplayItems.Add(item);
                }
            }
            else
            {
                try
                {
                    var target =
                       from item in Items
                       where
                           (SearchByCode && item.Code == SearchText)
                           ||
                           (SearchByName && item.Name.Contains(SearchText))
                       select item;
                    foreach (var item in DisplayItems.Except(target).ToArray())
                    {
                        DisplayItems.Remove(item);
                    }
                    foreach (var item in target.Except(DisplayItems).ToArray())
                    {
                        DisplayItems.Add(item);
                    }
                }
                catch { }
            }
        }
    }
}
