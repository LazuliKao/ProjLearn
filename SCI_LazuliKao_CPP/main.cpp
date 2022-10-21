#include <iostream>
class AutoPart
{
public:
	AutoPart(std::string name, std::string code, std::string type,int count):
		name(name), code(code), type(type), count(count);
	~AutoPart();
	std::string name,code,type;
	int count;  
private: 
};   
int main()
{
	std::cout<<"输入数量："<<std::endl;
	int count;
	std::cin>>count;
	std::cout << "输入单件：" << std::endl;
	std::vector<AutoPart> items= std::vector<AutoPart>();
	for (int i=0; i<count; i++) {
		std::string name, code, type;
		int count;
		std::cout << "输入名称：" << std::endl;
		std::cin >> name  ;
		std::cout << "输入编号：" << std::endl;
		std::cin >>  code ;
		std::cout << "输入类型：" << std::endl;
		std::cin >> type;
		std::cout << "输入数量" << std::endl;
		std::cin >> count;
		AutoPart part(name, code, type, count);
		items.push_back(part);
	}
	std::cout << "名称\t编号\t类型\t数量" << std::endl;
	for (auto& part : items)
	{
		std::cout << part. << std::endl;


	}
}