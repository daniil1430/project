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
        return Math.abs(key.hashCode() % size);
    }

    public void put(K key, V value) {
        int idx = hash(key);
        List<K> bucketKeys = keys.get(idx);
        List<V> bucketValues = values.get(idx);

        int pos = bucketKeys.indexOf(key);
        if (pos >= 0) {
            bucketValues.set(pos, value);
        } else {
            bucketKeys.add(key);
            bucketValues.add(value);
        }
    }

    public V get(K key) {
        int idx = hash(key);
        List<K> bucketKeys = keys.get(idx);

        int pos = bucketKeys.indexOf(key);
        if (pos >= 0) {
            return values.get(idx).get(pos);
        }
        return null;
    }

    public boolean remove(K key) {
        int idx = hash(key);
        List<K> bucketKeys = keys.get(idx);
        List<V> bucketValues = values.get(idx);

        int pos = bucketKeys.indexOf(key);
        if (pos >= 0) {
            bucketKeys.remove(pos);
            bucketValues.remove(pos);
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return "{}";
    }
}