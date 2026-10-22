package com.cgvsu.rasterizationfxapp;

import com.cgvsu.rasterization.Ellipse;
import com.cgvsu.rasterization.Rasterization;
import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class RasterizationController {

    @FXML
    private Canvas canvas;

    @FXML
    public void initialize() {
        GraphicsContext gc = canvas.getGraphicsContext2D();

        Rasterization.drawRectangle(gc, 200, 300, 200, 100, Color.CHOCOLATE);
        Rasterization.drawRectangle(gc, 250, 250, 50, 200, Color.AQUA);

        drawEllipse(gc, 400, 200, 150, 80, Color.BLUE);
        drawEllipse(gc, 150, 460, 100, 60, Color.RED);
        drawEllipse(gc, 600, 450, 60, 60, Color.GREEN);
        drawEllipse(gc, 700, 150, 40, 100, Color.PURPLE);
    }

    private void drawEllipse(GraphicsContext gc, int xc, int yc, int a, int b, Color color) {
        gc.setStroke(color);
        gc.strokeOval(xc - a, yc - b, a * 2, b * 2);
    }
}