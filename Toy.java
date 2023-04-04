// Класс для игрушки
// id игрушки,
// текстовое название,
// количество
// частота выпадения игрушки (вес в % от 100)

// import java.util.*;
// import java.text.*;
// import java.io.*;

public class Toy {
    private Integer id; //id игрушки;
    private String name; // текстовое название
    private int amount; // количество
    private int chance; //частота выпадения


    public Toy(Integer id, String description) {
        this.id = id;
        this.name= description;
        this.amount = 0;
        this.chance = 0;
    }


    public Integer getId() {
        return this.id;
    }


    public String getName() {
        return this.name;
    }


    public Integer getAmount() {
        return this.amount;
    }


    public void setAmount(Integer amount) {
        this.amount = amount;
    }


    public Integer getChance() {
        return this.chance;
    }


    public void setChance(Integer chance) {
        this.chance = chance;
    }
    
}
