template <typename K, typename V>
class Dictionary {
    private:
    std::map<K,V> m;
     
    public:
    const V& get(const K& key) const {
        return m[key];
    }
 
    void set(const K& key, const V& value) {
        m[key] = value;
    }
};