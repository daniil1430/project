package ru.vsu.cs.oop.tolubaev_d_i.my_hash_map;

import java.util.ArrayList;
import java.util.List;

public class MyHashMultiMap<K, V> {

    private List<List<K>> keys;
    private List<List<List<V>>> values;
    private int size;

    public MyHashMultiMap() {
    }

    private int hash(K key) {
        return 0;
    }

    public void put(K key, V value) {
    }

    public List<V> get(K key) {
        return null;
    }

    public boolean removeKey(K key) {
        return false;
    }

    @Override
    public String toString() {
        return "{}";
    }
}