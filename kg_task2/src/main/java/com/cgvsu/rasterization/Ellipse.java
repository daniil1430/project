package com.cgvsu.rasterization;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class Ellipse {

    public static void draw(GraphicsContext gc, int xc, int yc, int a, int b, Color color) {
        double step = 0.01;

        for (double t = 0; t <= 2 * Math.PI; t += step) {
            int x = (int) Math.round(xc + a * Math.cos(t));
            int y = (int) Math.round(yc + b * Math.sin(t));

            gc.setFill(color);
            gc.fillRect(x, y, 1, 1);
        }
    }

    public static void drawByBoundingBox(GraphicsContext gc, int x0, int y0, int width, int height, Color color) {
        int xc = x0 + width / 2;
        int yc = y0 + height / 2;
        int a = width / 2;
        int b = height / 2;

        draw(gc, xc, yc, a, b, color);
    }
}