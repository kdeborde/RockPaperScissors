#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <random>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->playerWinCountLbl->setText(QString::number(playerWinCount));
    ui->programWinCountLbl->setText(QString::number(programWinCount));

    buttonGroup = new QButtonGroup(this);
    buttonGroup -> addButton(ui->rockRadioButton);
    buttonGroup -> addButton(ui->paperRadioButton);
    buttonGroup -> addButton(ui->scissorsRadioButton);

    connect(ui->SubmitBtn, &QPushButton::clicked, this, &MainWindow::onSubmitButtonClicked);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::onSubmitButtonClicked()
{
    QAbstractButton *checkedRadioButton = buttonGroup->checkedButton();
    if (checkedRadioButton == ui->rockRadioButton)
    {
        playGame("Rock");
    }
    else if (checkedRadioButton == ui->paperRadioButton)
    {
        playGame("Paper");
    }
    else if (checkedRadioButton == ui->scissorsRadioButton)
    {
        playGame("Scissors");
    }
}

void MainWindow::playGame(QString playerChoice)
{
    QString programChoice = getProgramChoice();
    ui->playerChoiceLabel->setText(playerChoice);
    ui->programChoiceLabel->setText(programChoice);

    playerChoice = playerChoice.toLower();
    programChoice = programChoice.toLower();

    if (playerChoice == programChoice)
    {
        ui->resultLabel->setText("It's a tie!");
    }
    else if (playerChoice == "rock" && programChoice == "scissors"
             || playerChoice == "paper" && programChoice == "rock"
             || playerChoice == "scissors" && programChoice == "paper")
    {
        playerWinCount++;
        ui->playerWinCountLbl->setText(QString::number(playerWinCount));
        ui->resultLabel->setText("Player Wins!");
    }
    else
    {
        programWinCount++;
        ui->programWinCountLbl->setText(QString::number(programWinCount));
        ui->resultLabel->setText("Computer Wins!");
    }
}

QString MainWindow::getProgramChoice()
{
    QString programChoice = "";
    std::random_device rand;
    std::mt19937 gen(rand());
    std::uniform_int_distribution<> distr(1, 3);

    int randomNumber = distr(gen);

    switch (randomNumber)
    {
    case 1:
        programChoice = "Rock";
        break;
    case 2:
        programChoice = "Paper";
        break;
    case 3:
        programChoice = "Scissors";
        break;
    default:
        programChoice = "It's broke";
    }
    return programChoice;
}
