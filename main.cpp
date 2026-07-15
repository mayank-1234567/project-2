#include<iostream>
#include<string>
#include<vector>
std:: vector<int>from_time;
std:: vector<int>to_time;
std::vector<std:: string>task;
std::vector<int>hours;
std::vector<std:: string>f_task;
int fixed_task(){
int i{1};
int from;
int to;
int c;
std::string tas;
while (i!=0){std::cout<<"tell fixed task"<<"\n";
std::getline(std::cin,tas);
task.push_back(tas);
std::cout<<"tell time for fixed task"<<"\n";
std::cout<<"from"<<"\n";
std::cin>>from;
std::cout<<"to"<<"\n";
std::cin>>to;
from_time.push_back(from);
to_time.push_back(to);
std::cout<<"to add more fixed task enter 1 or to switch to flexible task enter 0"<<"\n";
std::cin>>c;
i=c;


}
return 0;
}

int flexible_task(){
int i{1};
int c;
std:: string n_task;
int hour;
while (i!=0){
std::cout<<"enter task"<<"\n";
std::cin>>n_task;
std::cout<<"number of hours"<<"\n";
std::cin>>hour;
f_task.push_back(n_task);
hours.push_back(hour);
std::cout<<"enter 1 or 0 "<<"\n";
std::cin>>c;
i=c;
}

return 0;
}
int main(){
fixed_task();
flexible_task();
return 0;
}
