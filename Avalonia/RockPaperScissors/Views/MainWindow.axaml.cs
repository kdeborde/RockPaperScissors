using Avalonia.Controls;
using Avalonia.Interactivity;
using Avalonia.LogicalTree;
using System;
using System.Linq;
using System.Windows;

namespace RockPaperScissors.Views
{
    public partial class MainWindow : Window
    {
        int playerWinCount;
        int programWinCount;
        public MainWindow()
        {
            playerWinCount = 0;
            programWinCount = 0;

            InitializeComponent();
        }

        public void PlayButton_Click(object sender, RoutedEventArgs args)
        {
            string playerChoice = "";
            string programChoice = GetProgramChoice();
            var PlayerChoiceRadioBtn = this.GetLogicalDescendants()
            .OfType<RadioButton>()
            .FirstOrDefault(r => r.GroupName == "RpsRadioGroup" && r.IsChecked == true);

            if (PlayerChoiceRadioBtn != null && PlayerChoiceRadioBtn.Name != null)
            {
                playerChoice = PlayerChoiceRadioBtn.Name;
                PlayerChoiceText.Content = playerChoice;
            }
            ProgramChoiceText.Content = programChoice;

            ResultText.Content = GetResult(playerChoice, programChoice);
            PlayerWinCountLabel.Content = playerWinCount;
            ProgramWinCountLabel.Content = programWinCount;
        }

        public string GetProgramChoice()
        {
            Random random = new Random();
            string programChoice;
            int randomNumber = random.Next(1, 4);
            switch (randomNumber)
            {
                case 1:
                    programChoice = "rock";
                    break;
                case 2:
                    programChoice = "paper";
                    break;
                case 3:
                    programChoice = "scissors";
                    break;
                default:
                    programChoice = "it's broke.";
                    break;
            }
            return programChoice;
        }

        public string GetResult(string playerChoice, string programChoice)
        {
            if (playerChoice == programChoice)
            {
                return "It's a tie!";
            }
            else if (playerChoice == "rock" && programChoice == "scissors"
                || playerChoice == "paper" && programChoice == "rock"
                || playerChoice == "scissors" && programChoice == "paper")
            {
                playerWinCount++;
                return "Player Wins!";
            }
            else
            {
                programWinCount++;
                return "Program Wins!";
            }
        }
    }
}