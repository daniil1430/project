package ru.vsu.cs.oop.tolubaev_d_i.my_hash_map;

import java.util.ArrayList;
import java.util.List;

public class MyHashMap<K, V> {

    private List<List<K>> keys = new ArrayList<>();
    private List<List<V>> values = new ArrayList<>();
    private int size = 16;

    public MyHashMap() {
        for (int i = 0; i < size; i++) {
            keys.add(new ArrayList<>());
            values.add(new ArrayList<>());
        }
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