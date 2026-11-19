package com.cgvsu.rasterization;

import javafx.scene.image.PixelWriter;
import javafx.scene.paint.Color;

public class Ellipse {

    public static void draw(PixelWriter pixelWriter, int xc, int yc, int a, int b, Color color) {
        int x = 0;
        int y = b;

        int a2 = a * a;
        int b2 = b * b;
        int twoA2 = 2 * a2;
        int twoB2 = 2 * b2;

        int p1 = b2 - a2 * b + a2 / 4;
        int dx = 0;
        int dy = twoA2 * y;

        while (dx < dy) {
            plotPoints(pixelWriter, xc, yc, x, y, color);
            x++;
            dx += twoB2;

            if (p1 < 0) {
                p1 += b2 + dx;
            } else {
                y--;
                dy -= twoA2;
                p1 += b2 + dx - dy;
            }
        }

        int p2 = (int) (b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2);

        while (y >= 0) {
            plotPoints(pixelWriter, xc, yc, x, y, color);
            y--;
            dy -= twoA2;

            if (p2 > 0) {
                p2 += a2 - dy;
            } else {
                x++;
                dx += twoB2;
                p2 += a2 - dy + dx;
            }
        }
    }

    private static void plotPoints(PixelWriter pixelWriter, int xc, int yc, int x, int y, Color color) {
        pixelWriter.setColor(xc + x, yc + y, color);
        pixelWriter.setColor(xc - x, yc + y, color);
        pixelWriter.setColor(xc + x, yc - y, color);
        pixelWriter.setColor(xc - x, yc - y, color);
    }

    public static void drawByBoundingBox(PixelWriter pixelWriter, int x0, int y0, int width, int height, Color color) {
        int xc = x0 + width / 2;
        int yc = y0 + height / 2;
        int a = width / 2;
        int b = height / 2;

        draw(pixelWriter, xc, yc, a, b, color);
    }
}