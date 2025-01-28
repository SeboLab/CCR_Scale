import launch
import launch_ros.actions

def generate_launch_description():

    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='rapport',
            executable='publisher_text',
            name='publisher_text'
        ),
        launch_ros.actions.Node(
            package='rapport',
            executable='subscriber_text',
            name='subscriber_text'
        ),
        launch_ros.actions.Node(
            package='rapport',
            executable='slides',
            name='slides'
        ),
    ])

if __name__=='__main__':
    generate_launch_description()
