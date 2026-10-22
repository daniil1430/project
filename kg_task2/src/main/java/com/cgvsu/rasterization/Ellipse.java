package com.cgvsu.rasterization;

import javafx.scene.image.PixelWriter;
import javafx.scene.paint.Color;

public class Ellipse {

    public static void draw(PixelWriter pixelWriter, int xc, int yc, int a, int b, Color color) {
        double step = 0.01;

        for (double t = 0; t <= 2 * Math.PI; t += step) {
            int x = (int) Math.round(xc + a * Math.cos(t));
            int y = (int) Math.round(yc + b * Math.sin(t));

            pixelWriter.setColor(x, y, color);
        }
    }

    public static void drawByBoundingBox(PixelWriter pixelWriter, int x0, int y0, int width, int height, Color color) {
    }
}