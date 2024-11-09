#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include <QUndoCommand>
#include <QFile>
#include <QFileDialog>
#include <QString>
#include <QTextEdit>
#include <QTextStream>
#include <QMessageBox>


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
    void on_actioncopy_triggered();

    void on_actionUndo_triggered();


    void on_mc_submitbtn_clicked();



    void on_ae_choosebtn_clicked();

    void on_mc_choosebtn_clicked();

private:
    Ui::MainWindow *ui;

    QString currentFile = "";
};
#endif // MAINWINDOW_H
