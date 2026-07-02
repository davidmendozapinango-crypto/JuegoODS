from pathlib import Path
from typing import List, Optional

from reports.gantt import gantt_frequencies
from reports.logs import game_logs
from reports.ranking import top_players
from reports.summary import player_summary


def export_report(
    report_type: str,
    file_path: str,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
) -> str:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    if report_type == "player_summary":
        lines.append("RESUMEN DE JUGADORES")
        lines.append("-" * 50)
        lines.append(f"{'Cédula':<15}{'Nombre':<25}{'Juegos':<10}")
        for row in player_summary(date_from, date_to):
            lines.append(
                f"{row['cedula']:<15}{row['full_name']:<25}{row['total_games']:<10}"
            )
    elif report_type == "gantt":
        lines.append("FRECUENCIA DE NÚMEROS SORTEADOS")
        lines.append("-" * 40)
        lines.append(f"{'Número':<15}{'Frecuencia':<15}")
        for number, freq in gantt_frequencies(date_from, date_to):
            lines.append(f"{number:<15}{freq:<15}")
    elif report_type == "logs":
        lines.append("HISTÓRICO DE JUEGOS")
        lines.append("-" * 60)
        lines.append(f"{'Fecha':<25}{'Jugador':<15}{'Ganador':<10}")
        for game in game_logs(date_from, date_to):
            lines.append(
                f"{game.played_at:<25}{game.player_id:<15}{game.winner_card:<10}"
            )
    elif report_type == "top5":
        lines.append("TOP 5 JUGADORES")
        lines.append("-" * 40)
        lines.append(f"{'Jugador':<15}{'Puntos':<15}")
        for cedula, score in top_players(date_from, date_to):
            lines.append(f"{cedula:<15}{score:<15}")
    else:
        raise ValueError("Tipo de reporte inválido")

    content = "\n".join(lines) + "\n"
    path.write_text(content, encoding="utf-8")
    return str(path)
