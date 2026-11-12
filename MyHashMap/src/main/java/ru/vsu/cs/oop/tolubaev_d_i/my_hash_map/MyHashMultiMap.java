package ru.vsu.cs.oop.tolubaev_d_i.my_hash_map;

import java.util.ArrayList;
import java.util.List;

public class MyHashMultiMap<K, V> {

    private List<List<K>> keys = new ArrayList<>();
    private List<List<List<V>>> values = new ArrayList<>();
    private int size = 16;

    public MyHashMultiMap() {
        for (int i = 0; i < size; i++) {
            keys.add(new ArrayList<>());
            values.add(new ArrayList<>());
        }
    }

    private int hash(K key) {
        return Math.abs(key.hashCode() % size);
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