#include "mainwindow.h"
#include "./ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_actionUndo_triggered()
{


}

void on_actioncopy_triggered()
{


}


void MainWindow::on_mc_submitbtn_clicked()
{
    if(ui ->mc_dupchecker->isChecked()){
        // QMessage box "Are you sure you want to overwrite? Y/N"

    }
    else{
        //Check directory, if output file is already present refuse to continue, "File Present, Unable to proceed."

        /* if(good){
         *
         run demucs

        } */
    }

}


void MainWindow::on_ae_choosebtn_clicked()
{
    QString filename = QFileDialog::getOpenFileName(this, "Select video file (.mp4)");
    QFile file(filename);        //QFile file(windowFilePath())

    if(filename.isEmpty()){

        return;
    }

    if(!file.open(QIODevice::ReadOnly)){

    QMessageBox::warning(this, "Error", "Unable to open file in read only mode");

    return;
}
    else{

    ui->ae_inpath->setText(filename);

}


}

void MainWindow::on_actioncopy_triggered()
{
    return;
}


void MainWindow::on_mc_choosebtn_clicked()
{
    QString filename = QFileDialog::getOpenFileName(this, "Select Audio file (.mp3)");
    QFile file(filename);        //QFile file(windowFilePath())

    if(filename.isEmpty()){

        return;
    }

    if(!file.open(QIODevice::ReadOnly)){

        QMessageBox::warning(this, "Error", "Unable to open file in read only mode");

        return;
    }
    else{

       // dirpath == cut file path


        // ui->mc_outpath->setText(dirpath)
        ui->mc_inpath->setText(filename);

    }

}

