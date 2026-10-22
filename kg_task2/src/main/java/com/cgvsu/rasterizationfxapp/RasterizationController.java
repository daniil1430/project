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

        Ellipse.draw(gc, 400, 200, 150, 80, Color.BLUE);
        Ellipse.drawByBoundingBox(gc, 50, 400, 200, 120, Color.RED);
        Ellipse.draw(gc, 600, 450, 60, 60, Color.GREEN);
        Ellipse.draw(gc, 700, 150, 40, 100, Color.PURPLE);
    }
}