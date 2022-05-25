from src.treport.report import Report, get_config

if __name__ == '__main__':
    parameters = {'p_start_date': '01.05.2022', 'p_end_date': '31.05.2022'}
    db_url, path_to_params_reports_file = get_config('run_report.ini')
    report = Report('treport_example', path_to_params_reports_file, parameters, db_url)

    if report.isCorrect:
        report.contentReport.save(report.outDir + report.report_file_name)
        report.logger.info(f'Файл {report.outDir + report.report_file_name} сохранен')