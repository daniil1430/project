package ru.vsu.cs.oop.tolubaev_d_i.my_hash_map;

import java.util.ArrayList;
import java.util.List;

public class MyHashMap<K, V> {

    private List<List<K>> keys;
    private List<List<V>> values;
    private int size;

    public MyHashMap() {
    }

    private int hash(K key) {
        return 0;
    }

    public void put(K key, V value) {
    }

    public V get(K key) {
        return null;
    }

    public boolean remove(K key) {
        return false;
    }

    @Override
    public String toString() {
        return "{}";
    }
}