package ru.vsu.cs.oop.tolubaev_d_i.my_hash_map;

public class Main {
    public static void main(String[] args) {
        MyHashMap<String, Integer> map = new MyHashMap<>();
        map.put("Сливы", 7);
        map.put("Виноград", 13);
        map.put("Бананы", 15);
        System.out.println("Сливы: " + map.get("Сливы"));
        System.out.println("Виноград: " + map.get("Виноград"));
        System.out.println("Бананы: " + map.get("Бананы"));
        map.remove("Виноград");
        System.out.println("После удаления Винограда: " + map.get("Виноград"));
        System.out.println(map);

        MyHashMultiMap<String, String> mm = new MyHashMultiMap<>();
        mm.put("Лавка 1", "Яблоки");
        mm.put("Лавка 1", "Арбузы");
        mm.put("Лавка 2", "Картошка");
        mm.put("Лавка 2", "Свекла");
    }
}