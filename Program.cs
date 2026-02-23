// (c) 2026 Guillermo Roger Hernandez Chandia - ADS

using Spectre.Console;
using System.Threading;

namespace CyberSentinel
{
    class Program
    {
        static void Main(string[] args)
        {
            // Criando o esqueleto da interface (Layout)
            var layout = new Layout("Root")
                .SplitRows(
                    new Layout("Header").Size(5),
                    new Layout("Body").SplitColumns(
                        new Layout("Sensors"),
                        new Layout("MainView")
                    )
                );

            // 1. O Cabeçalho (Título Futurista)
            layout["Header"].Update(
                new Panel(Align.Center(new FigletText("CYBER SENTINEL").Color(Color.Aqua)))
                    .Border(BoxBorder.None));

            // 2. Sensores Laterais
            layout["Sensors"].Update(
                new Panel(new Rows(
                    new Text("FIREWALL: [ACTIVE]", new Style(Color.Lime)),
                    new Text("ENCRYPTION: [256-BIT]", new Style(Color.Blue)),
                    new Text("SCANNER: [ON]", new Style(Color.Yellow))
                )).Header("SYSTEM CORE").Border(BoxBorder.Double));

            // 3. Área Principal (A Mágica acontece aqui)
            AnsiConsole.Live(layout).Start(ctx =>
            {
                var table = new Table().Centered().BorderColor(Color.Grey);
                table.AddColumn("TARGET");
                table.AddColumn("STATUS");
                
                layout["MainView"].Update(new Panel(table).Header("THREAT SCANNER").BorderColor(Color.Aqua));
                ctx.Refresh();

                string[] alvos = { "192.168.1.105", "Port 8080", "Mainframe DB", "Auth Gateway" };
                foreach (var alvo in alvos)
                {
                    Thread.Sleep(1000);
                    table.AddRow(alvo, "[bold green]SECURE[/]");
                    ctx.Refresh();
                }
            });
        }
    }
}