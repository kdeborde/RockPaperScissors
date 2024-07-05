#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QButtonGroup>
#include <QLabel>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void onSubmitButtonClicked();

private:
    Ui::MainWindow *ui;
    QButtonGroup *buttonGroup;
    QString getProgramChoice();
    void playGame(QString playerChoice);
    int playerWinCount = 0;
    int programWinCount = 0;
};
#endif // MAINWINDOW_H
