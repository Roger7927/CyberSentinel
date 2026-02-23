// (c) 2026 Guillermo Roger Hernandez Chandia - ADS

using Spectre.Console;
using System;
using System.Threading;

namespace CyberSentinel
{
    class Program
    {
        static void Main(string[] args)
        {
            AnsiConsole.Clear();
            double angle = 0;

            // Criamos o layout inicial para o cockpit
            var layout = new Layout("Root")
                .SplitColumns(
                    new Layout("Radar"),
                    new Layout("Logs")
                );

            AnsiConsole.Live(layout).Start(ctx =>
            {
                while (true)
                {
                    // 1. Criando o Canvas do Zero (A Caixa de Desenho)
                    var canvas = new Canvas(40, 40);
                    int centerX = 20, centerY = 20, radius = 15;

                    // 2. Desenho Geométrico (Borda e Varredura)
                    for (int i = 0; i < 360; i += 2)
                    {
                        double rad = i * Math.PI / 180;
                        canvas.SetPixel(centerX + (int)(radius * Math.Cos(rad)), centerY + (int)(radius * Math.Sin(rad)), Color.DeepSkyBlue1);
                    }

                    double sweepRad = angle * Math.PI / 180;
                    for (int r = 0; r < radius; r++)
                    {
                        canvas.SetPixel(centerX + (int)(r * Math.Cos(sweepRad)), centerY + (int)(r * Math.Sin(sweepRad)), Color.Lime);
                    }

                    // 3. Atualizando os Painéis (Lógica ADS de Refresh)
                    layout["Radar"].Update(new Panel(canvas).Header("[bold aqua]🛰️ LIVE RADAR[/]").BorderColor(Color.Grey));
                    layout["Logs"].Update(new Panel(new Text($"\n[INFO] SCANNING ANGLE: {angle}°\n[ALERT] TARGETS DETECTED: 2", new Style(Color.Lime))).Header("SYSTEM LOGS"));

                    angle = (angle + 15) % 360;
                    ctx.Refresh(); // O comando de mestre que não falha
                    Thread.Sleep(50);
                }
            });
        }
    }
}