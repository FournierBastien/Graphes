
using namespace std;

template <typename key_type, typename val_type>
class Graphe{

    public:
    
    std::map<key_type,val_type> nodes;
    std::set<std::pair<key_type,key_type> > connections;
};