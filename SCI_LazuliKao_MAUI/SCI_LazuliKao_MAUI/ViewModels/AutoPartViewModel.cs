
using Newtonsoft.Json;
using Prism.Commands;
using Prism.Mvvm;
using System.Collections.ObjectModel;

namespace SCI_LazuliKao_MAUI.ViewModels
{
    public class AutoPartViewModel : BindableBase
    {
        private Action<AutoPartViewModel> _removeThis;
        [JsonIgnore] public Action<AutoPartViewModel> RemoveThisFunc { set => _removeThis = value; }
        public AutoPartViewModel() { }
        public AutoPartViewModel(Action<AutoPartViewModel> removeThis)
        {
            _removeThis = removeThis;
        }
        private string code = "";
        public string Code
        {
            get { return code; }
            set { SetProperty(ref code, value); }
        }
        private string name = "";
        public string Name
        {
            get { return name; }
            set { SetProperty(ref name, value); }
        }
        private string type = "";
        public string Type
        {
            get { return type; }
            set { SetProperty(ref type, value); }
        }
        private int count;
        public int Count
        {
            get { return count; }
            set { SetProperty(ref count, value); }
        }
        private DelegateCommand _remove;
        [JsonIgnore]
        public DelegateCommand Remove =>
                _remove ??= new DelegateCommand(() =>
                {
                    _removeThis(this);
                });
        [JsonIgnore]
        public AutoPartViewModel Self
        {
            get { return this; }
        }
    }
}
