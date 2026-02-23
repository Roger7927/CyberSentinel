// (c) 2026 Guillermo Roger Hernandez Chandia - ADS

using System;
using System.Threading;
using Spectre.Console;

namespace CyberSentinel
{
    class Program
    {
        static void Main(string[] args)
        {
            // Título Impactante (Visual Futurista)
            AnsiConsole.Write(
                new FigletText("CYBER SENTINEL")
                    .Centered()
                    .Color(Color.Aqua));

            var panel = new Panel(new Text("SISTEMA DE MONITORAMENTO DE REDE ATIVO", new Style(Color.Lime)));
            panel.Border = BoxBorder.Double;
            AnsiConsole.Write(panel);

            // Simulação de Carregamento de Módulos (UX Profissional)
            AnsiConsole.Status()
                .Start("Iniciando protocolos de defesa...", ctx => 
                {
                    ctx.Spinner(Spinner.Known.Dots);
                    ctx.SpinnerStyle(Style.Parse("bold blue"));

                    Thread.Sleep(2000);
                    AnsiConsole.MarkupLine("[grey]LOG:[/] Módulos de Criptografia... [green]OK[/]");
                    Thread.Sleep(1000);
                    AnsiConsole.MarkupLine("[grey]LOG:[/] Scanner de Perímetro... [green]OK[/]");
                });

            // Lógica de Varredura (O Coração do Sistema)
            var table = new Table().Centered();
            table.AddColumn("PROCESSO");
            table.AddColumn("STATUS");
            table.AddColumn("RISCO");

            AnsiConsole.Live(table)
                .Start(ctx =>
                {
                    string[] processos = { "Injeção de SQL", "Ataque Brute Force", "Port Scan", "Phishing Link" };
                    Random rnd = new Random();

                    for (int i = 0; i < processos.Length; i++)
                    {
                        Thread.Sleep(1500);
                        string risco = rnd.Next(1, 100) > 70 ? "[red]ALTO[/]" : "[yellow]BAIXO[/]";
                        table.AddRow(processos[i], "[bold green]ANALISADO[/]", risco);
                        ctx.Refresh();
                    }
                });

            AnsiConsole.MarkupLine("\n[bold aqua]VARREDURA CONCLUÍDA. NENHUMA AMEAÇA CRÍTICA DETECTADA NO MOMENTO.[/]");
        }
    }
}