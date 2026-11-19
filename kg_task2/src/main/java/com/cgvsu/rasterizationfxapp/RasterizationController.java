package com.cgvsu.rasterizationfxapp;

import com.cgvsu.rasterization.Ellipse;
import com.cgvsu.rasterization.Rasterization;
import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;
import javafx.scene.image.PixelWriter;
import javafx.scene.paint.Color;

public class RasterizationController {

    @FXML
    private Canvas canvas;

    @FXML
    public void initialize() {
        PixelWriter pixelWriter = canvas.getGraphicsContext2D().getPixelWriter();

        Rasterization.drawRectangle(canvas.getGraphicsContext2D(), 200, 300, 200, 100, Color.CHOCOLATE);
        Rasterization.drawRectangle(canvas.getGraphicsContext2D(), 250, 250, 50, 200, Color.AQUA);

        Ellipse.draw(pixelWriter, 400, 200, 150, 80, Color.BLUE);
        Ellipse.drawByBoundingBox(pixelWriter, 50, 400, 200, 120, Color.RED);
        Ellipse.draw(pixelWriter, 600, 450, 60, 60, Color.GREEN);
        Ellipse.draw(pixelWriter, 700, 150, 40, 100, Color.PURPLE);
    }
}