using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace version_11._4
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public bool instance_f6 = true;
        public MainWindow()
        {
            InitializeComponent();
        }

        private void F6_Click(object sender, RoutedEventArgs e)
        {

            if (instance_f6)
            {
                F6 f6 = new F6();
                f6.Owner = this;
                f6.Show();
                instance_f6 = false;
            }
        }
    }
}
