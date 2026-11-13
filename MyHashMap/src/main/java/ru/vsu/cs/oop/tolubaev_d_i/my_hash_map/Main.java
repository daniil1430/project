package ru.vsu.cs.oop.tolubaev_d_i.my_hash_map;

public class Main {
    public static void main(String[] args) {
        MyHashMap<String, Integer> map = new MyHashMap<>();
        map.put("Сливы", 7);
        map.put("Виноград", 13);
        map.put("Бананы", 15);
        System.out.println(map);
        System.out.println("Бананы: " + map.get("Бананы"));
    }
}